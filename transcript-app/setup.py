from setuptools import setup, find_packages

setup(
    name='transcript-app',
    version='0.1',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    install_requires=[
        'tkinter',
        'sounddevice',
        'soundfile',
        'SpeechRecognition',
        'deep-translator',
        'wordcloud',
        'matplotlib',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'transcript-app=main:main',  # Assuming main.py has a main function to start the app
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python application for recording meetings and generating transcripts.',
    url='https://github.com/yourusername/transcript-app',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)