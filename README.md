# template_content_generator
generating template content such as about us, news artical, news title, product description and etc. using pretrained Language Model GPT-3

Key conceptes and techniques that are fundamental to using the OpenAI API for any task including:
* Content generation
* Summarization
* Classification, categorization, and sentiment analysis
* Data extraction
* Translation etc.

## Introduction
The OpenAI API can be applied to virtually any task that involves understanding or generating natural language or code.

GPT-3 or the third generation of Generative Pre-trained Transformer, is a neural network machine learning model trained 
using internet data to generate any type of text. It requires a small amount of input text to generate large volumes of 
relevant and sophisticated machine-generated text.

GPT-3's deep learning neural network is a model with over 175 billion machine learning parameters. As a result GPT-3 is
better than any prior model for producing text that is convincing enough to seem like a human could have written it.

The `completions` endpoint is the core of OpenAI API and provides a simple interface that's extremenly flexible and powerful.\
You input some text as a prompt, and the API will return a text completion that attempts to match whatever instructions or 
context we gave it.\
You can think of this as a very advanced autocomplete - the model processes your text prompt and tries to predict what's 
most likely to come next. Designing the prompt is essentially how we "program" the model.\
In many cases, it's helpful to both show and tell the model what you want. Adding examples to the prompt can help communicate
patterns or nuances.

## What can GPT-3 do?
Natural Language processing includes as one of its major components natural langauge generation. which focus on generating
human langauge natural text. However, generating human understandable content is a challenge for machines that don't really
know the complexities and nuances of language. Using text on the internet, GPT-3 is trained to generate realistic human text.

GPT-3 has been used to create articles, poetry, stories, news reports and dialogue using just a small amount of input text
that can be used to produce large amounts of quality copy.

GPT-3 is also being used for automated conversational tasks, responding to any text that a person types into the computer 
with a new piece of text appropriate to the context. GPT-3 can create anything with a text structure, and not just human 
language text. It can also automatically generate text summarizations and even programming code.

## How does GPT-3 work?
GPT-3 is a language prediction model. This means that it has a neural network machine learning model that can take input
text as an input and transform it into what it predicts the most useful result will be. This is accomplished by training 
the system on the vast body of internet text to spot patterns. More specifically, GPT-3 is the third version of a model
that is focused on text generation based on being pre-trained on a huge amount of text.

## Prompt Design
There are three basic guidelines to creating prompts:
1. `Show and tell`: Make it clear what you want either through instructions, examples, or a combination of the two. If
you want the model to rank a list of items in alphabetical order or to classify a paragraph by sentiment, show it that's
what you want.
2. `Provide quality data`: If you're trying to build a classifier or get the model to follow a pattern, make sure that
there are enough examples. The model is usually smart enough to see through basic spelling mistakes and give you a response,
but it also might assume this is intentional, and it can affect the response.
3. `Check your settings`: The temperature and top_p settings control how deterministic the model is in generaating a response.

## Model Request body
 * `prompt`: The prompt to generate complitions for, encoded as string, array of strings, array of tokens, or array of 
token array. `<|endoftext|>` is the document seperator that the model sees during training, so if a prompt is not specified 
the model will generate as if from the beginning of a new document.
 * `engine`: **_text-davinci-001_** is the most capable GPT-3 model. Can do any task the other models can do, often with
 less context. In addition to responding to prompt, also supports inserting completions within text.
 * `temperature`: temperature means what sampling temperature to use. Higher value means the model will take more risks, 
we can use 0.9 for more creative applications, and 0 for ones with a well-defined answer.\
Remember that the model predicts which text is most likely to follow the text preceding it. Temperature is a value between
0 and 1 that essentially lets you control how confident the model should be when making these predictions. Lowering temperature
means it will take fewer risks, and completions will be more accurate and deterministic. Increasing temperature will result
in more diverse completions.
 * `max_tokens`: The maximum number of tokens to generate in complition. Most model have context length of 2048.
 * `top_p`: An alternative to sampling with temperature, called nucleus sampling. where the model considers the result of 
the tokens with top_p probability mass, so 0.1 means only the tokens comprising the top 10% probability mass are considered
 * `frequency_penalty`: Positive values penalize new tokens based on their existing frequency in the text so far, decreasing
the model's likelihood to repeat the same line.
 * `presence_penalty`: Positive value penalize new tokens based on whether they appear in the text so far, increasing 
the model's likelihood to talk about new topics.

# Development Setup

If you don't have `pip` on your system, you can download it with the help of this command:

```commandline
sudo apt-get install python3-pip
```

## Virtual Environment Setup
You can create a virtual environment with Anaconda if you have it on your system, create a virtualenv with command below:

```commandline
conda create -n yourenvname python==x.x
conda activate yourenvname
```

Or you can install virtualwrapper with command below:

```commandline
sudo pip3 install virtualenvwrapper
sudo pip3 install --upgrade virtualenv
```

And after installation create virtual environment:

```commandline
cd/your/path && mkvirtualenv --python=python3 yourenvname
```

Install the required packages from the requirements.txt to run this project:

```commandline
pip install -r requirements.txt
```

## Project Essentials Guide
To run this project the most important thing is to have a secret API key from OpenAI that enables the model to generate
the contents. If you have the secret API key you should set it as your environment variable under tha name of 
`OPENAI_API_KEY` and read it using `python-dotenv` package.
