# ----------------------------------------------
# Listing Available Audio Files (stored locally)
# ----------------------------------------------

# File Discovery Module

from pathlib import Path
import sys

# Root Path
# Replace Placeholder plath with your actual file path 🛣️

Ageless_Root = Path("</path/to/your/desired/root>")
print(Ageless_Root)


# Recording Dir Path
Audio_Dir = Ageless_Root / "</designated/path>"
print(Audio_Dir)



"""
Unlike voice_files[] list, which is a static list, this module uses list_recordings() & get_recordings()
list_recordings() detects newly added recordings without restarting the backend.
get_recording() retrieves a file directly by name, avoiding list-index lookups.
This keeps file discovery dynamic and retrieval separate from the API routes.
"""

# Stress Time Complexity Calculation may be done later, when optimising for performance

# recordings listing
def list_recordings():
    """Return available WAV recording filenames."""
    return sorted(
        file.name
        for file in Audio_Dir.glob("*.wav")
        if file.is_file()
    )



def get_recording(record_name: str):
    """Return the path of a specific WAV recording."""

    # Prevent path traversal
    if Path(record_name).name != record_name:
        return None

    file_path = Audio_Dir / record_name

    if file_path.is_file() and file_path.suffix.lower() == ".wav":
        return file_path

    return None



# Primitive logic of voice_files []
# using .globe to see all audio files as a 'list'
# voice_files = [
#     file.name
#     for file in Audio_Dir.glob("*.wav")
# ]
# print(voice_files)


# Later, Files will be shown in sorted order, newest first


