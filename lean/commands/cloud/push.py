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

from typing import Optional

import click

from lean.click import LeanCommand


@click.command(cls=LeanCommand, requires_cli_project=True)
@click.option("--project", type=str, help="Name or id of the project to push (all local projects if not specified)")
def push(project: Optional[str]) -> None:
    """Push local projects to QuantConnect.

    This command overrides the content of cloud files with the content of their respective local counterparts.
    """
    # TODO: Implement
    print(project)
