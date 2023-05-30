# Automated Content Generation with Python

This project showcases the power of Python in automating content generation for popular platforms like YouTube. By leveraging tools such as Jinja, MoviePy, and Reddit's API, you can effortlessly transform Reddit posts into engaging videos with just a single click.

## Game play Video

[Gameplay] (https://drive.google.com/file/d/1my1cdN3NKcZQsJXnwHfj3xMHFGkbdl44/view?usp=sharing)

## Demonstration

- [YouTube](https://youtu.be/m_wNpWcPIEs)

## Features

- Automatically fetches content from Reddit using the Reddit API
- Utilizes Jinja to convert the content into provided templates for screenshots
- Incorporates MoviePy for video editing and generation
- Generates high-quality videos with captivating visuals and audio
- Allows customization options to tailor the content to your preferences

## Getting Started

### Prerequisites

To run this project, make sure you have the following installed:

- Python 3
- Jinja2 library
- MoviePy library
- gTTS
- praw

### Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/iamuv2000/reddit-yt.git
```

2. Navigate to the project directory.

```bash
cd reddit-yt
```

3. Install the required Python libraries.

### Usage

1. Open the `reddit.py` file and enter your Reddit API credentials.

```python
# Reddit API credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
```

2. Customize the settings in `main.py` according to your preferences.

```python
# Customize settings
subreddit_name = 'AskReddit'  # Choose the subreddit you want to fetch content from
videos_to_generate = 10  # Number of posts to fetch
```

3. Run the script to generate the automated content.

```bash
python main.py
```

4. Sit back and watch as the script fetches content, captures screenshots, and generates a captivating video for your YouTube channel or Instagram page!

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [MoviePy](https://github.com/Zulko/moviepy)
- [PRAW (Python Reddit API Wrapper)](https://github.com/praw-dev/praw)

Feel free to customize and enhance this README file based on your specific project details and requirements.
