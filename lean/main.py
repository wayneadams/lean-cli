# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean CLI v1.0. Copyright 2021 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import traceback
from io import StringIO

import click
from pydantic.error_wrappers import ValidationError

from lean.commands import lean
from lean.container import container
from lean.models.errors import MoreInfoError


def main() -> None:
    """This function is the entrypoint when running a Lean command in a terminal."""
    try:
        lean.main(standalone_mode=False)
    except Exception as exception:
        logger = container.logger()
        logger.debug(traceback.format_exc().strip())

        if isinstance(exception, ValidationError) and hasattr(exception, "input_value"):
            logger.debug("Value that failed validation:")
            logger.debug(exception.input_value)
            logger.error(f"Error: {exception}")
        elif isinstance(exception, MoreInfoError):
            logger.error(f"Error: {exception}")
            logger.error(f"Visit {exception.link} for more information")
        elif isinstance(exception, click.UsageError):
            io = StringIO()
            exception.show(file=io)

            exception_str = io.getvalue().strip()
            exception_str = exception_str.replace("Try 'lean", "\nTry 'lean")
            exception_str = exception_str.replace("for help.",
                                                  "for help or go to the following url for a list of common errors:\nhttps://www.quantconnect.com/docs/v2/lean-cli/user-guides/troubleshooting")

            logger.info(exception_str)
        elif isinstance(exception, click.Abort):
            logger.info("Aborted!")
        else:
            logger.error(f"Error: {exception}")

        sys.exit(1)
