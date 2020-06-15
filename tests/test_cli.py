import pytest
from hr import cli


@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_arguments(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_succeds_with_a_path(parser):
    """
    with a path,the parser shoutld exit with an error.
    """
    with pytest.raises(SystemExit):
        args=parser.parse_args(['/some/path'])
        assert args.path=='/some/path'

def test_parser_export_flag(parser):
    """
    The export value should default to Falsee, but set
    to True when passed to the parser.
    """
    args = parser.parse_args(['/some/path'])
    assert args.export==False

    args = parser.parse_args(['--export','/some/path'])
    assert args.export==True


