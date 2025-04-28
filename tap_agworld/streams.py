"""Stream type classes for tap-agworld."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_agworld.client import AgWorldStream

SCHEMAS_DIR = resources.files(__package__) / "schemas"


class CompaniesStream(AgWorldStream):
    """Define custom stream."""

    name = "companies"
    path = "/companies"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "companies.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row


class SeasonsStream(AgWorldStream):
    """Define custom stream."""

    name = "seasons"
    path = "/seasons"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "seasons.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row

    def get_child_context(sef, record: dict, context: t.Optional[dict]) -> dict:
        return {
            "season_id": record["id"],
        }


class SeasonFieldsStream(AgWorldStream):
    """Define custom stream."""

    parent_stream_type = SeasonsStream
    ingnore_parent_replication_key = True

    name = "season_fields"
    path = "/seasons/{season_id}/fields"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "fields.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row


class FieldsStream(AgWorldStream):
    """Define custom stream."""

    name = "fields"
    path = "/fields"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    replication_method = "INCREMENTAL"
    schema_filepath = SCHEMAS_DIR / "fields.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row


class ActivitiesStream(AgWorldStream):
    """Define custom stream."""

    name = "activities"
    path = "/activities"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "activities.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row


class FarmsStream(AgWorldStream):
    """Define custom stream."""

    name = "farms"
    path = "/farms"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "farms.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row


class CollectionJobsStream(AgWorldStream):
    """Define custom stream."""

    name = "collection_jobs"
    path = "/collection_jobs"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "updated_at"
    schema_filepath = SCHEMAS_DIR / "collection_jobs.json"

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        row["updated_at"] = row["attributes"]["updated_at"]
        return row
