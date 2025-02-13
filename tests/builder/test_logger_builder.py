import sys
from unittest.mock import MagicMock
from unittest.mock import patch

from spikify.builder.logger_builder import LoggerBuilder


class TestLoggerBuilder:
    @patch("spikify.builder.logger_builder.loguru_logger")
    def test_add_sys_stdout(self, mock_loguru_logger):
        # Arrange
        logger_builder = LoggerBuilder()
        mock_loguru_logger.add = MagicMock()

        # Act
        logger_builder.add_sys_stdout(level="DEBUG", log_format="custom_format")

        # Assert
        mock_loguru_logger.add.assert_called_once_with(
            sys.stdout, level="DEBUG", format="custom_format"
        )

    @patch("spikify.builder.logger_builder.loguru_logger")
    def test_add_file(self, mock_loguru_logger):
        # Arrange
        logger_builder = LoggerBuilder()
        mock_loguru_logger.add = MagicMock()

        # Act
        logger_builder.add_file(
            file_path="log.log",
            level="INFO",
            log_format="custom_format",
            log_filter="custom_filter",
            colorize=True,
            serialize=True,
            backtrace=False,
            diagnose=False,
            enqueue=False,
            context="custom_context",
            catch=False,
            rotation="1 week",
            retention="1 month",
            compression="zip",
            delay=True,
            watch=True,
            mode="w",
            buffering=2,
            encoding="utf-16",
            errors="replace",
            newline="\r\n",
            closefd=False,
            opener="custom_opener",
        )

        # Assert
        mock_loguru_logger.add.assert_called_once_with(
            "log.log",
            level="INFO",
            format="custom_format",
            filter="custom_filter",
            colorize=True,
            serialize=True,
            backtrace=False,
            diagnose=False,
            enqueue=False,
            context="custom_context",
            catch=False,
            rotation="1 week",
            retention="1 month",
            compression="zip",
            delay=True,
            watch=True,
            mode="w",
            buffering=2,
            encoding="utf-16",
            errors="replace",
            newline="\r\n",
            closefd=False,
            opener="custom_opener",
        )

    @patch("spikify.builder.logger_builder.loguru_logger")
    def test_get_logger(self, mock_loguru_logger):
        # Arrange
        logger_builder = LoggerBuilder()
        mock_loguru_logger.add = MagicMock()

        # Act
        logger = logger_builder.get_logger()

        # Assert
        assert logger is mock_loguru_logger
