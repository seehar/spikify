import nox


@nox.session(python=["3.8", "3.9", "3.11", "3.12"], venv_backend="conda")
def pytest(session):
    session.install("poetry")

    # 设置 Poetry 使用当前环境
    session.env["POETRY_VIRTUALENVS_IN_PROJECT"] = "false"
    session.env["POETRY_VIRTUALENVS_CREATE"] = "false"

    session.run_always("poetry", "install", "--all-extras", "--no-root", external=True)
    session.run("poetry", "install", "--all-extras", "--no-root")
    session.run("poetry", "run", "pytest", "-s", "--forked")
