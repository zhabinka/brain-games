install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-prime:
	poetry run brain-prime

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression
