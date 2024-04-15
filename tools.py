from crewai_tools import BaseTool


class TweeterTweetsOpinionsFinder(BaseTool):
    name: str = "TweeterTweetsOpinionsFinder"
    description: str = """
            Tool to find tweets opinions based on the article and key insights.
            input is the article and key insights.
            output is the tweets opinions.
        """

    def _run(self, article: str, key_insights: str) -> str:
        return str(
            {
                "tweets": [
                    {
                        "content": "Iran attacking Israel was 'reckless'. Journalist: What would Britain do if our consulate was flattened? David Cameron: Well, w-we would take very strong action... Journalist: Iran would say that's what they did..."
                    },
                    {
                        "content": "US Rules Out Joining Israeli Attack Against Iran. Israel Strikes Gaza Refugee Camp. UN Chief Urges Peace In UN Security Council Meeting On Iran's Israel Strikes. Israeli Attacks On Defenceless Innocent Palestinians Civilians Women Children Barbaric Genocide.",
                    },
                    {
                        "content": "When Israel came out of Egypt the Amalekites fought against them and God declared that He'll destroy the enemy. Years later He sent Saul who compromised and many years down the line, came Haman with a sole mission of destroying Israel but God intervened."
                    },
                    {
                        "content": "Missiles sent from Iran being intercepted by the Iron Dome in Israel's capital city Tel Aviv. Is this the start of World War 3? This is going to be tough.",
                    },
                    {
                        "content": "Lebanon has indicated a potential escalation in tensions with Israel. Prime Minister Najib Mikati emphasized that while Lebanon is not inclined towards conflict, it cannot tolerate continued Israeli aggression. He asserted Lebanon's rejection of the violation of its airspace by Israeli forces."
                    },
                ]
            }
        )
