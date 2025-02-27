"""Pytest-BDD Hooks for Test Execution."""
from typing import Any
from pytest import FixtureRequest
from main.core.utils.custom_logger import CustomLogger
# from main.core.api.request_manager import RequestManager

LOGGER = CustomLogger(__name__)

def pytest_bdd_before_scenario(request: FixtureRequest, feature: Any, scenario: Any):
    """Hook executed before each scenario.
    Parameters
    ----------
    request: FixtureRequest
        Fixture request object
    feature: Feature
        pytest bdd feature object
    scenario: Scenario
        pytest bdd scenario object
    """
    # feature_name = getattr(feature, "name", "Unknown Feature")
    LOGGER.info(f"STARTED FEATURE \"{feature.name}\"")
    LOGGER.info(f"STARTED SCENARIO \"{scenario.name}\"")
    request.context = {}
    request.tags = {}
    request.body = {}
    request.response = {}

def pytest_bdd_after_scenario(request: FixtureRequest, scenario: Any):
    """Hook executed after each scenario.
    Parameters
    ----------
    request: FixtureRequest
        Fixture request object
    feature: Any
        pytest bdd feature object
    scenario: Any
        pytest bdd scenario object
    """
    scenario_report = request.node.__scenario_report__.serialize()
    failed_steps = [
        step['name'] for step in scenario_report['steps'] if step['failed']
    ]
    status = 'FAILED' if failed_steps else 'SUCCESS'

    LOGGER.info(f"FINISHED SCENARIO \"{scenario.name}\" WITH STATUS: {status}\n")

    if failed_steps:
        LOGGER.info(f"Failed Steps: {', '.join(failed_steps)}")
