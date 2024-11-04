from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    author="XinZhu",
    description="A simple math quiz game",
    url="https://github.com/236de/XinZhu_DSSS_HW2",
)
