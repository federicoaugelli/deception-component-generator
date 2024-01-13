# deception-component-generator
Cybersecurity project

## methods
- get /bin/.git/config
- get /modules/.git/config
- get /app/.git/config
- get /laravel/.env
- get /api/.env
- get /.env
- get /files/.git/config
- get /downloads/.git/config
- get /log/.git/config
- get /alive.php
- get /showLogin.cc
- get /vendor/.git/config
- get /Public/home/js/check.js
- get /sitemap.xml



## Project 2 - Deception component generator
Cybersecurity experts have recently proposed using defensive deception as a means to leverage the information asymmetry typically enjoyed by attackers as a tool for defenders. By creating fake services and components that appear as valuable targets to attackers, defenders can divert the attacker's attention and resources away from critical assets. Attackers might spend time and effort trying to compromise these fake elements, leaving less capacity to target actual valuable assets. The goal of this project is to create a fake resource generator for one specific type of resource.
Specification
The final output of the generator must be a OCI compatible image ready to be instantiated
The container image must include all the relevant "fake" data for its correct operation
The container must function out of the box, eventual configuration has to be provided during the generation to build the final working image
You can choose one of the following resource types to implement
## rest API server
form an openAPI specification implement a dumb service with fake/random data
accept configurations for oauth authentication (at generation time ) to secure the api endpoint and provide an out of the box functionality
## References
You can use LLM to generate the data, but it is better to use a local first model instead of relying on web api like chatGPT.
https://python.langchain.com/docs/integrations/llms/llamacpp
https://medium.com/@karankakwani/build-and-run-llama2-llm-locally-a3b393c1570e
