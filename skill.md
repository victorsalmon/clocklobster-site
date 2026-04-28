# Skill: Build Theme ZIP

## Trigger
Only use this skill when the user **explicitly asks** you to output a new theme build, create a theme ZIP, package the theme, or prepare it for WordPress upload. Do not run this automatically on every session.

## Description
Package the `clocklobster-theme/` directory into a timestamped ZIP file suitable for WordPress theme upload.

## Context
- This project follows the conventions in `AGENTS.md`.
- The theme folder is `clocklobster-theme/` in the project root.
- WordPress requires the ZIP to contain a single root folder matching the theme slug, with `style.css` inside it.

## Steps

1. Read `AGENTS.md` for project context and conventions.
2. Verify `clocklobster-theme/style.css` exists and contains a valid WordPress theme header.
3. Ensure the `build/` directory exists (create it if missing).
4. Delete any previous `build/clocklobster-theme-*.zip` files to avoid accumulation.
5. Generate a timestamp in `YYYYMMDD-HHMMSS` format.
6. Create the ZIP:
   - Source: `clocklobster-theme/`
   - Destination: `build/clocklobster-theme-{timestamp}.zip`
7. Verify the ZIP structure: the root entry must be `clocklobster-theme/`, not individual files.
8. Report the path of the created ZIP file.
9. Update `docs/CHANGELOG.md` if this is part of a release task.
10. Update `to-do.md` if applicable.

## Example Command (PowerShell)
```powershell
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
Remove-Item build/clocklobster-theme-*.zip -ErrorAction SilentlyContinue
Compress-Archive -Path clocklobster-theme -DestinationPath "build/clocklobster-theme-$timestamp.zip"
```

## Verification
Extract the ZIP temporarily and confirm the first directory is `clocklobster-theme/`.
