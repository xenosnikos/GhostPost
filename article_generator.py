from langchain.document_loaders import UnstructuredURLLoader
from langchain import OpenAI, LLMChain, PromptTemplate
import logging


def generate_article(url, title, description):
    loader = UnstructuredURLLoader(urls=[url])
    llm = OpenAI(temperature=0, max_tokens=1000)

    try:
        data = loader.load()

        prompt_template = """Don't return empty results. You must write an interesting long article based on the 
        following text and try to avoid using and copying same words from the text. Divide result article into 
        several paragraphs using html <p> tags. 

            {text}
            """
        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        content = llm_chain.run(data[0].page_content)

        prompt_template = """Below is given article title.

        {title}

        Generate new article title changing the words slightly but making sure there's no mention of the source, meaning omit everything after the dash."""

        prompt = PromptTemplate(template=prompt_template, input_variables=["title"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        title = llm_chain.run(title)

        if description is not None:
            prompt_template = """Below is new given article description.

            {description}

            Generate new article description which is very different from above description but similar in meaning.
            """
            prompt = PromptTemplate(template=prompt_template, input_variables=["description"])
            llm_chain = LLMChain(prompt=prompt, llm=llm)
            description = llm_chain.run(description)

        return {"title": title, "description": description, "content": content}
    except Exception as e:
        print(f"Error generating article: {str(e)}")
        logging.info(f"Generated article with title: {title}")
        return {"title": "", "description": "", "content": ""}

