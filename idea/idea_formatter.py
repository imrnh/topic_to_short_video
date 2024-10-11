import xml.etree.ElementTree as ET
import json


def xml_to_json(xml_data):
    root = ET.fromstring(xml_data)

    video_ideas = [
        {
            "Title": video.find('Title').text,
            "Keywords": [keyword.strip() for keyword in video.find('Keywords').text.split(',')]
        }
        for video in root.findall('VideoIdea')
    ]
    video_ideas_json = json.loads(json.dumps(video_ideas, indent=4))    

    return video_ideas_json




# if __name__ == "__main__":
#     sample_xml_data = """
#         <VideoIdeas>
#             <VideoIdea>
#                 <Title>Sugar vs. Artificial Sweeteners: Which is Healthier?</Title>
#                 <Keywords>Artificial Sweeteners, Harmful effect of Artificial Sweeteners, Why sugar is bad?</Keywords>
#             </VideoIdea>
#             <VideoIdea>
#                 <Title>Sugar vs. Artificial Sweeteners: Which is Healthier?</Title>
#                 <Keywords>Artificial Sweeteners, Harmful effect of Artificial Sweeteners, Why sugar is bad?</Keywords>
#             </VideoIdea>
#         </VideoIdeas>
#     """

#     print(xml_to_json(sample_xml_data))