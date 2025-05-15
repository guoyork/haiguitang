import os
from django.core.management.base import BaseCommand
from user_inputs.models import Questions
from django.conf import settings


class Command(BaseCommand):
    help = 'Create Question instances from puzzle markdown files'

    def handle(self, *args, **options):
        puzzle_dir = os.path.join(settings.BASE_DIR, 'puzzles')
        
        # Get all existing titles to check for duplicates
        existing_titles = set(Questions.objects.values_list('title', flat=True))
        
        created_count = 0
        skipped_count = 0
        
        for filename in os.listdir(puzzle_dir):
            if filename.endswith('.md'):
                with open(os.path.join(puzzle_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract title from filename
                title = filename[:-3]  # Remove .md extension
                
                # Skip if title already exists
                if title in existing_titles:
                    self.stdout.write(self.style.NOTICE(f'Skipped duplicate: {title}'))
                    skipped_count += 1
                    continue
                
                # Extract question and answer
                sections = content.split('### ')
                question = sections[1].replace('汤面\n\n', '').strip()
                answer = sections[2].replace('汤底\n\n', '').strip()
                
                # Create and save Question
                Questions.objects.create(
                    title=title,
                    question=question,
                    answer=answer
                )
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created question: {title}'))
                existing_titles.add(title)  # Add to existing titles to prevent duplicates in same run

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {created_count} questions, skipped {skipped_count} duplicates'
        ))
