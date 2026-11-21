from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

## few shot prompting

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "You are a translator"
        },
        {
            "role": "user", "content": """Translate these sentences from English to Spanish:
            'Helo' -> 'Hola',
            'Goodbye' -> 'Adios',

            Now translate: 'Halted'.
            """
        }
    ]
)

# print(completion.choices[0].message.content)

## Direct prompting


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "You are an helpful assistant"
        },
        {
            "role": "user", "content": "What is the capital of Minas Gerais?"
        }
    ]
)

# print(completion.choices[0].message.content)


## Chain of thought prompting

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "You are an helpful assistant"
        },
        {
            "role": "user", "content": "Answer the following question explaing your reasoning step by step: What is the capital of Minas Gerais?"
        }
    ]
)

# print(completion.choices[0].message.content)

# Instructional prompting

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "You are a knowledgeable and experienced personal trainer"
        },
        {
            "role": "user", "content": "Write a 300 word summary of the benefits of exercise, using bullet points."
        }
    ]
)

# print(completion.choices[0].message.content)

## Role-playing prompting

# import json
# from fpdf import FPDF

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a soviet soldier fighting on a building during the Stalingrad battle. Reply with JSON only.",
#         },
#         {
#             "role": "user",
#             "content": """Tell me the current situation you are facing and what you expect in the next days.
#             Return JSON with this shape:
#             {
#               "title": "short document title",
#               "date": "a date in late 1942",
#               "location": "where you are",
#               "paragraphs": ["four or five paragraphs of the field record"]
#             }
#             Write it as a professional historical field record. No markdown.
#             """,
#         },
#     ],
# )

# document = json.loads(completion.choices[0].message.content)

# FONT = "/System/Library/Fonts/Supplemental"
# INK = (42, 28, 18)
# RULE = (92, 64, 44)


# class HistoricalRecord(FPDF):
#     def header(self):
#         self.set_fill_color(250, 246, 235)
#         self.rect(0, 0, 210, 297, "F")
#         self.set_draw_color(*RULE)
#         self.set_line_width(0.7)
#         self.rect(12, 12, 186, 273)
#         self.set_line_width(0.2)
#         self.rect(14, 14, 182, 269)

#     def footer(self):
#         self.set_y(-20)
#         self.set_font("Record", "I", 9)
#         self.set_text_color(*RULE)
#         self.cell(0, 8, str(self.page_no()), align="C")


# pdf = HistoricalRecord(format="A4")
# pdf.set_auto_page_break(auto=True, margin=26)
# pdf.set_margins(24, 28, 24)
# pdf.add_font("Record", "", f"{FONT}/Times New Roman.ttf")
# pdf.add_font("Record", "B", f"{FONT}/Times New Roman Bold.ttf")
# pdf.add_font("Record", "I", f"{FONT}/Times New Roman Italic.ttf")
# pdf.add_page()

# pdf.set_text_color(*RULE)
# pdf.set_font("Record", "I", 10)
# pdf.cell(0, 6, "HISTORICAL FIELD RECORD", align="C", new_x="LMARGIN", new_y="NEXT")
# pdf.ln(6)

# pdf.set_text_color(*INK)
# pdf.set_font("Record", "B", 18)
# pdf.multi_cell(0, 9, document["title"], align="C")
# pdf.ln(2)

# pdf.set_text_color(*RULE)
# pdf.set_font("Record", "I", 11)
# pdf.multi_cell(0, 6, f"{document['date']}   ·   {document['location']}", align="C")
# pdf.ln(3)
# pdf.set_draw_color(*RULE)
# pdf.line(55, pdf.get_y(), 155, pdf.get_y())
# pdf.ln(8)

# pdf.set_text_color(*INK)
# pdf.set_font("Record", "", 12)
# for paragraph in document["paragraphs"]:
#     pdf.multi_cell(0, 7, paragraph, align="J")
#     pdf.ln(4)

# pdf.output("role-playing.pdf")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "You are a travel blogger"
        },
        {
            "role": "user", "content": "Write a 500 word blog post about your recent trip to Brazil."
        }
    ],
    temperature=0.9,
    stream=True,
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
    print("\n")
