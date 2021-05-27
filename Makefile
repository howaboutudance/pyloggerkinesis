BUILD_TAG = hematite/pyecslogger
INTERACT_TAG = ${BUILD_TAG}-interact
TEST_TAG = ${BUILD_TAG}-test
ECR_TAG = public.ecr.aws/g8z1b4q2/pystandlogger:latest
DOCKER_BUILD=docker build ./ -f Dockerfile.ecs
DOCKER_RUN=docker run
VENV_VERSION_FOLDER := venv$(shell python3 --version | sed -ne 's/[^0-9]*\(\([0-9]\.\)\{0,2\}\).*/\1/p' | sed -e "s/\.//g")

init-env: FORCE
	python3 -m venv ./$(VENV_VERSION_FOLDER)
	( \
		source ./$(VENV_VERSION_FOLDER)/bin/activate; \
		pip3 install --use-feature=2020-resolver -r requirements.txt; \
		pip3 install --use-feature=2020-resolver -r requirements-dev.txt; \
	)

build: FORCE
	${DOCKER_BUILD} --no-cache=true --target=app -t ${BUILD_TAG}

build-dev: FORCE
	${DOCKER_BUILD} --target=app -t ${BUILD_TAG}

publish: build
	docker tag ${BUILD_TAG} ${ECR_TAG} 
	docker push ${ECR_TAG}

run:
	${DOCKER_RUN} ${BUILD_TAG}

interact: FORCE
	${DOCKER_BUILD} --target=interact -t ${INTERACT_TAG}
	${DOCKER_RUN} -it ${INTERACT_TAG}

test: FORCE
	${DOCKER_BUILD} --target=test -t ${TEST_TAG}
	${DOCKER_RUN} -it ${TEST_TAG}

local-test: FORCE
	tox
	mypy pystandlogger/

FORCE: