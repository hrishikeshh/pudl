"""Validate post-ETL EIA 923 data and associated derived outputs."""

import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.mark.eia923
@pytest.mark.post_etl
def test_frc_eia923(pudl_out_eia):
    """Sanity checks for EIA 923 Fuel Recepts and Costs output."""
    logger.info("Reading EIA 923 Fuel Receipts and Costs data...")
    logger.info(
        f"Successfully pulled {len(pudl_out_eia.frc_eia923())} records.")


@pytest.mark.eia923
@pytest.mark.post_etl
def test_gf_eia923(pudl_out_eia):
    """Sanity checks for EIA 923 Generator Fuel output."""
    logger.info("Reading EIA 923 Generator Fuel data...")
    logger.info(f"Successfully pulled{len(pudl_out_eia.gf_eia923())} records.")


@pytest.mark.eia923
@pytest.mark.post_etl
def test_bf_eia923(pudl_out_eia):
    """Sanity checks for EIA 923 Boiler Fuel output."""
    logger.info("Reading EIA 923 Boiler Fuel data...")
    logger.info(
        f"Successfully pulled {len(pudl_out_eia.bf_eia923())} records.")


@pytest.mark.eia923
@pytest.mark.post_etl
def test_gen_eia923(pudl_out_eia):
    """Sanity checks for EIA 923 Generation output."""
    logger.info("Reading EIA 923 Generation data...")
    logger.info(
        f"Successfully pulled {len(pudl_out_eia.gen_eia923())} records.")