from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup

def get_video_title(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text)

  link = soup.find_all(name = "title")[0]
  title = str(link)
  title = title.replace("<title>", "")
  title = title.replace("</title>", "")

  return title

def get_video_info(url_video, language=["en"], translation=None):
  print("Inside get video info"+language)

  video_loader = YoutubeLoader.from_youtube_url(
      url_video,
      language=language,
      translation=translation,
  )

  print("Inside get video info")
  print(video_loader.language)
  infos = video_loader.load()[0]
  transcript = infos.page_content
  video_title = get_video_title(url_video)
  print("Inside get video info"+language)

  return transcript, video_title


def llm_chain():
  system_prompt = "You are a helpful virtual assistant answering a query based on a video transcript, which will be provided below."

  inputs = "Query: {query} \n Transcript: {transcript}"

  user_prompt = "{}".format(inputs)

  prompt_template = ChatPromptTemplate.from_messages([
      ("system", system_prompt),
      ("user", user_prompt)
  ])

  ### Loading the LLM
  llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.1, max_tokens=None, timeout=None, max_retries=2)

  chain = prompt_template | llm | StrOutputParser()

  return chain

def interpret_video(url, query="summarize in a clear and understandable way", language=["en"], translation=None):

  print("inside interpret video"+language)
  try:
    load_dotenv()
    transcript, video_title = get_video_info(url, language, translation)

    video_infos = f"""## Video info:

    Title: {video_title}
    URL: {url}

    """

    output_language = ". answer in english"

    chain = llm_chain()

    t = "\n## What is the video about? \n"
    res = chain.invoke({"transcript": transcript, "query": "explain in 1 sentence what this video is about {}".format(output_language)})
    about = t + res

    t = "\n## Main topics \n"
    res = chain.invoke({"transcript": transcript, "query": "list the topics of this video {}".format(output_language)})
    main_topics = t + res

    t = "\n## Response to query \n"
    res = chain.invoke({"transcript": transcript, "query": query})
    response = t + res

    return video_infos, about, main_topics, response


  except Exception as e:
    print("Error loading transcript")
    return "Error loading transcript: {}".format(e), "", "", ""