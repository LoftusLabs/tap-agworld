"""AgWorld tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_agworld import streams


class TapAgWorld(Tap):
    """AgWorld tap class."""

    name = "tap-agworld"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType(),
            required=False,
            description="A string of the API token used by the api_token header auth ",
        ),
        th.Property(
            "start_date",
            th.DateTimeType(nullable=True),
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType(nullable=False),
            title="API URL",
            default="https://api.mysample.com",
            description="The url for the API service",
        ),
        th.Property(
            "page_size",
            th.IntegerType,
            required=False,
            description="The number of records to return per page. Defaults to 10 and maximum is 100.",
        ),
        th.Property(
            "records_jsonpath",
            th.StringType,
            required=True,
            description="a jsonpath string representing the path in the requests "
            "response that contains the records to process. Defaults "
            "to `$[*]`. Stream level records_path will overwrite "
            "the top-level records_path",
        ),
        th.Property(
            "flattening_enabled",
            th.BooleanType,
            description="",
        ),
        th.Property(
            "flattening_max_depth",
            th.IntegerType,
            description="",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.AgWorldStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CompaniesStream(self),
            streams.SeasonsStream(self),
            streams.SeasonFieldsStream(self),
            streams.FieldsStream(self),
            streams.ActivitiesStream(self),
            streams.FarmsStream(self),
            # streams.CollectionJobsStream(self)
        ]


if __name__ == "__main__":
    TapAgWorld.cli()
