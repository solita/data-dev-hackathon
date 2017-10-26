.PHONY=deploy delete

TEMPLATE:=infra-template.yml
PROFILE:=PROFILE_HERE
STACK_NAME:=STACK_NAME_HERE

deploy:
	aws --profile ${PROFILE} cloudformation create-stack --stack-name ${STACK_NAME} --template-body file://${TEMPLATE} --capabilities CAPABILITY_IAM
	
delete:
	aws --profile ${PROFILE} cloudformation delete-stack --stack-name ${STACK_NAME}
