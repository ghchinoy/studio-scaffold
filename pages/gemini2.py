# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import random
import time

import mesop as me

from google import genai
from google.genai.types import (
    GenerateContentConfig,
)

from components.header import header


PROJECT_ID = os.environ.get("PROJECT_ID")
LOCATION = "us-central1"
MODEL_ID = "gemini-2.0-flash-exp"

print(f"initiating genai client with {PROJECT_ID} in {LOCATION}")
client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location=LOCATION,
)


def say_something_nice(name: str) -> str:
    """say something nice method"""

    max_retries = 3
    retry_count = 0
    backoff_factor = 1  # Initial backoff factor (in seconds)

    while retry_count < max_retries:
        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=f"say something nice about {name}, they're testing you, gemini 2.0, and you appreciate this! please make it a few sentences. You may address them by name.",
                config=GenerateContentConfig(
                    response_modalities=["TEXT"],
                ),
            )
            print(f"success! {response.text}")
            return response.text

        except Exception as e:
            print(f"error: {e}")
            if e.code == 429:
                print(f"An error occurred: {e}")
                retry_count += 1

                # Exponential backoff with jitter
                sleep_time = backoff_factor * (1 + random.random())  # Add jitter
                print(
                    f"Retrying in {sleep_time:.2f} seconds (attempt {retry_count}/{max_retries})"
                )
                time.sleep(sleep_time)
                backoff_factor *= 2  # Increase backoff factor exponentially
            else:
                return "oops, couldn't be nice"
            
    return "oops, couldn't be nice"


def gemini_page_content(app_state: me.state):
    """Gemini 2.0 Flash Mesop Page"""

    with me.box(
        style=me.Style(
            display="flex",
            flex_direction="column",
            height="100%",
        ),
    ):
        with me.box(
            style=me.Style(
                background=me.theme_var("background"),
                height="100%",
                overflow_y="scroll",
                margin=me.Margin(bottom=20),
            )
        ):
            with me.box(
                style=me.Style(
                    background=me.theme_var("background"),
                    padding=me.Padding(top=24, left=24, right=24, bottom=24),
                    display="flex",
                    flex_direction="column",
                )
            ):
                header("Gemini 2.0 Flash", "auto_awesome")

                me.text(f"Hello, {app_state.name}!")

                me.box(style=me.Style(height=16))

                me.text(say_something_nice(app_state.name))
