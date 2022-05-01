from click.testing import CliRunner
from hello import hello_tool

def test_hello():
    runnner = CliRunner()
    result = runnner.invoke(hello_tool,["--name","Samir","--color","blue"])
    assert "Samir" in result.output