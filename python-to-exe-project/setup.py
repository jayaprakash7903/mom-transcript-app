from setuptools import setup, find_packages

setup(
    name='MeetingMoMMaker',
    version='1.0',
    description='A Python application for recording meetings, transcribing audio, translating text, and generating word clouds.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'sounddevice',
        'soundfile',
        'SpeechRecognition',
        'deep-translator',
        'wordcloud',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'meeting_mom_maker=Transcript:main',  # Adjust if you have a main function
        ],
    },
    python_requires='>=3.6',
)