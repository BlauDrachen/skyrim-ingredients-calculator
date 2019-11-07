import os
import click
from app import create_app, db
from flask_migrate import Migrate

# config
app = create_app(os.getenv('ESICALC_ADMIN') or 'default')
migrate = Migrate(app, db)

# shell context
@app.shell_context_processor
def make_shell_context():
    return dict()


@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().discover(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
