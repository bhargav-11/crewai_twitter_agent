# crewai_twitter_agent

## Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/crewai_twitter_agent.git
    ```

2. Install the required dependencies:
    ```bash
    poetry install
    ```

3. Create a `.env` file in the root directory of the project and add the necessary environment variables. For example:
    ```plaintext
    OPENAI_API_KEY=sk-...
    SERPER_API_KEY=...
    TWITTER_BEARER_TOKEN=...
    ```

4. Run the script:
    ```bash
    python crew_twitter.py --url URL_OF_ARTICLE
    ```

    Replace `URL_OF_ARTICLE` with the actual URL of the article you want to process.
