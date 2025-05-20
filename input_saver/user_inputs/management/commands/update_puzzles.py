import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Update puzzles.json with all .md files in puzzles directory'

    def handle(self, *args, **options):
        puzzles_dir = os.path.join(settings.BASE_DIR, 'puzzles')
        json_path = os.path.join(puzzles_dir, 'puzzles.json')

        # Get all .md files
        md_files = [f for f in os.listdir(puzzles_dir) if f.endswith('.md')]

        # Read existing json
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                existing = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing = []

        # Merge and deduplicate
        updated = list(set(existing + md_files))
        updated.sort()  # Keep sorted for consistency

        # Write back
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(updated, f, ensure_ascii=False, indent=4)

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {json_path} with {len(md_files)} .md files'))
