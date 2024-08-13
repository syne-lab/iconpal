
guard-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

parser:
	antlr4 -visitor -Dlanguage=Python3 policy_parser/Policy.g4

# ARGS="-s 1 -p 5"
preprocess-dataset:
	python preprocess_dataset.py $(ARGS)


build: guard-NAMESPACE
	docker build \
	--tag ${NAMESPACE}/policy-generator:latest \
	--build-arg hugging_face_token=${HUGGING_FACE_HUB_TOKEN} \
	--build-arg openai_api_key=${OPENAI_API_KEY} \
	--build-arg gid=$$(id -g) \
	--build-arg uid=$$(id -u) \
	--build-arg user=$$(whoami) \
	--file Dockerfile \
	.

cache_diretory = ${HOME}/remote-store/policy-generator/cache/

# M=GPT3_5_Turbo make full-experiment
full-experiment:
	for r in "1" "2" "3";do \
		for exp_conf in "ablation" "tutorial" "example-type" "example-count" "temperature";do \
			ARGS="-m $(M) -p 100 -r $$r -c $$exp_conf --reprompt-count 0 $(E)" make policy-translation; \
		done \
	done

# E="--override --dry-run" make full-semantic-validation
# for exp_conf in "ablation" "tutorial" "example-count" "example-type" "temperature" "custom";do
full-semantic-validation:
	for m in "GPT4_1106_Preview" "GPT3_5_Turbo" "Llama_2_70b_Chat_Quant" "Mixtral_8x7b_0_1_Instruct" "Mistral_7b_0_1_Instruct" "Yi_34b_Chat" "Llama_2_13b_Chat" ;do \
		for exp_conf in "ablation" "tutorial" "example-count" "example-type" "temperature" "custom";do \
			for r in "1" "2" "3";do \
				ARGS="-d evaluations/$${exp_conf}/output/$${m}/p100/r$${r} -m GPT3_5_Turbo $(E)" make semantic-validation; \
			done \
		done \
	done

# M=GPT3_5_Turbo make full-syntax-validation
# for exp_conf in "ablation" "tutorial" "example-count" "example-type" "temperature" "custom";do
full-syntax-validation:
	for exp_conf in "ablation" "tutorial" "example-count" "example-type" "temperature" "custom";do \
		for r in "1" "2" "3";do \
			ARGS="-d evaluations/$${exp_conf}/output/$(M)/p100/r$${r} -a generated_policy $(E)" make syntax-validation; \
		done \
	done

# M=Mistral_7b_0_1_Instruct R=1 make full-result-analysis
full-result-analysis:
	for exp_conf in "ablation" "tutorial" "example-count" "example-type";do \
		ARGS="-d evaluations/$${exp_conf}/output/$(M)/p100/r$(R) -o evaluations/$${exp_conf}/output/$(M)/p100/r$(R)/results.csv --reprompt-count 0" make result-analysis; \
	done

# ARGS="-m Llama_2_70b_Chat_Quant -c custom -p 100 --reprompt-count 2 --endpoint https://jmpl2j4npg30xn-31211.proxy.runpod.net" make policy-translation
# ARGS="-m GPT3_5_Turbo -c custom -p 100 --reprompt-count 2" make policy-translation
# ARGS="-m Llama_2_13b_Chat -c custom -p 100 --reprompt-count 2 --endpoint https://u8tyc1k1az835n-31211.proxy.runpod.net" make policy-translation
# ARGS="-m GPT4_1106_Preview -c custom -p 100 --reprompt-count 2" make policy-translation
# ARGS="-m Mistral_7b_0_1_Instruct -c custom -p 100 --reprompt-count 2 --endpoint https://u8tyc1k1az835n-31211.proxy.runpod.net" make policy-translation
# ARGS="-m Mixtral_8x7b_0_1_Instruct -c custom -p 100 --reprompt-count 2 --endpoint https://u8tyc1k1az835n-31211.proxy.runpod.net" make policy-translation
# ARGS="-m Yi_34b_Chat -c custom -p 100 --reprompt-count 2 --endpoint https://u8tyc1k1az835n-31211.proxy.runpod.net" make policy-translation

policy-translation:
	docker run --net llm-gateway --rm -v ./:/home/$$(whoami)/app/ -v $(cache_diretory):/home/$$(whoami)/.cache/ ${NAMESPACE}/policy-generator python policy_translator.py $(ARGS); \

# ARGS="-d evaluations/ablation/output/Llama_2_70b_Chat/p5/r2 -a generated_policy" make syntax-validation
syntax-validation:
	docker run --net llm-gateway --rm -v ./:/home/$$(whoami)/app/ -v $(cache_diretory):/home/$$(whoami)/.cache/ ${NAMESPACE}/policy-generator python syntax_validity_checker.py  $(ARGS)

# ARGS="-m GPT4_1106_Preview -d evaluations/custom/output/GPT4_1106_Preview/p100/r1 --dry-run" make semantic-validation
semantic-validation:
	docker run --net llm-gateway --rm  -v ./:/home/$$(whoami)/app/ -v $(cache_diretory):/home/$$(whoami)/.cache/ ${NAMESPACE}/policy-generator  python semantic_validity_checker.py $(ARGS); \

clean:
	docker rmi $$(docker images | grep none | awk '{print $$3}')
