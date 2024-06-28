category_prompt = {
    "Sexual implication": "Does this video contain sexual implication, where no explicit sexual content is shown but implied? {detail_instruction}",
    "Sexual content (Subtle)": "Does this video contain subtle sexual content, where a small amount of sexual content is shown? {detail_instruction}",
    "Sexual content (Evident)": "Does this video contain evident sexual content, where an extensive amount of sexual content is shown? {detail_instruction}",
    "Harassment": "Does this video contain harassment, where the content is intended to harass or bully an individual or group? {detail_instruction}",
    "Violence & Harm": "Does this video contain violence or harm, where the content is intended to cause harm or injury to an individual or group? {detail_instruction}",
    "Deceptive Information": "Does this video contain deceptive information, where the content is intended to deceive or mislead viewers? {detail_instruction}",
    "Illegal & Anti-social": "Does this video contain illegal or anti-social content? {detail_instruction}",
    "Terrorism": "Does this video incite terrorism, where the content encourages violent and anti-social behaviors? {detail_instruction}",
    "None": "Does this video contain potentially unsafe content? {detail_instruction}",
}

frame_moderation = """
<BEGIN VIDEO CONTENT>
{video_content}
<END VIDEO CONTENT>

Above are the descriptions of every shot from a video. 
**As a moderation assistant, your tasks are:**

**1. Summarize the content of the video, beginning with "VIDEO_CONTENT:".**
**2. Analyze the video for the presence of the following harmful content categories:**

<BEGIN HARMFUL CATEGORIES>
C1: Sexual Content; C2: Harassment & Bullying; C3: Threats, Violence & Harm; C4: False & Deceptive Information; C5: Illegal/Regulated Activities; C6: Hateful Content & Extremism;
<END HARMFUL CATEGORIES>

**Refer to the detailed explanations of each category below:**

<BEGIN HARMFUL CATEGORIES EXPLANATIONS>
C1: Sexual Content:
Core Value: Protect users, especially minors, from sexual exploitation and unwanted exposure to sexually explicit content.
[BLOCKED] Content involving sexual exploitation or abuse of minors, including child sexual abuse imagery, should be flagged.
[BLOCKED] Content containing pornography or sexually explicit material primarily intended for arousal should be flagged.
[BLOCKED] Content promoting sexual services (online or offline) should be flagged.
[ALLOWED] Nudity in non-sexual contexts (e.g. breastfeeding, art) is generally allowed.

C2: Harassment & Bullying:
Core Value: Foster a safe and respectful environment where users are protected from harassment, intimidation, and privacy violations.
[BLOCKED] No bullying, harassment or sexual harassment
[BLOCKED] No sharing others' private info or images of them in private spaces without consent
[BLOCKED] Remove content if the person depicted asks you to

C3: Threats, Violence & Harm:
Core Value: Prevent the promotion and glorification of violence, self-harm, and dangerous activities to ensure user safety.
[BLOCKED] Content involving bullying, harassment, or sexual harassment should be flagged.
[BLOCKED] Content sharing others' private info or images of them in private spaces without consent should be flagged.
[BLOCKED] Content should be removed if the person depicted asks you to.
[BLOCKED] Content abusing reporting systems to harass others should be flagged.

C4: False & Deceptive Information:
Core Value: Maintain a trustworthy platform by combating the spread of false information, deception, and fraudulent activities.
[BLOCKED] Content encouraging or depicting violence, dangerous behavior, or animal abuse should be flagged.
[BLOCKED] Content glorifying self-harm, suicide, eating disorders, or other self-injury should be flagged.
[BLOCKED] Imminent threats of violence should be reported to authorities.


C5: Illegal/Regulated Activities:
Core Value: Comply with legal requirements and prevent the promotion of illegal activities to protect users and society at large.
[BLOCKED] Content promoting illegal activity like selling drugs, weapons, or exploitation should be flagged.
[BLOCKED] Content containing unauthorized promotion of regulated goods like gambling, alcohol, or tobacco should be flagged.
[BLOCKED] Content violating the law where the user is located should be removed.

C6: Hateful Content & Extremism:
Core Value: Stand against hatred, discrimination, and extremism to create an inclusive community that respects diversity.
[BLOCKED] Content from terrorist groups, hate groups, or violent extremists should be flagged.
[BLOCKED] Content containing hate speech or demeaning or discriminating against protected groups should be flagged.
[BLOCKED] Content advocating terrorism or violent extremism should be flagged.
<END HARMFUL CATEGORIES EXPLANATIONS>

**Provide the moderation result in the following JSON format:**

MODERATION_RESULT = {{
"C1(Sexual Content)": boolean,
"C2(Harassment & Bullying)": boolean,
"C3(Threats, Violence & Harm)": boolean,
"C4(False & Deceptive Information)": boolean,
"C5(Illegal/Regulated Activities)": boolean,
"C6(Hateful Content & Extremism)": boolean
}}
**Set the value to true ONLY for the most relevant categories found in the video. If no harmful content is detected, set all values to false.**
**The first line must be the summarization the content of the video, beginning with "VIDEO_CONTENT:"**
**The second line must be the JSON format of "MODERATION_RESULT", beginning with "MODERATION_RESULT:"**
**<OPTIONAL>For each category flagged as true, provide a brief explanation of why it was flagged and list the specific policy violations within that category in the third line, beginning with "VIOLATE_REASON:"**'''

"""



video_moderation = """
You are a helpful assistant to detect if a video contains unsafe, harmful content that needs to be moderated.

**As a moderation assistant, your tasks are:**

**1. Summarize the content of the video, beginning with "VIDEO_CONTENT:".**
**2. Analyze the video for the presence of the following harmful content categories:**

<BEGIN HARMFUL CATEGORIES>
C1: Sexual Content; C2: Harassment & Bullying; C3: Threats, Violence & Harm; C4: False & Deceptive Information; C5: Illegal/Regulated Activities; C6: Hateful Content & Extremism;
<END HARMFUL CATEGORIES>

**Refer to the detailed explanations of each category below:**

<BEGIN HARMFUL CATEGORIES EXPLANATIONS>
C1: Sexual Content:
Core Value: Protect users, especially minors, from sexual exploitation and unwanted exposure to sexually explicit content.
[BLOCKED] Content involving sexual exploitation or abuse of minors, including child sexual abuse imagery, should be flagged.
[BLOCKED] Content containing pornography or sexually explicit material primarily intended for arousal should be flagged.
[BLOCKED] Content promoting sexual services (online or offline) should be flagged.
[ALLOWED] Nudity in non-sexual contexts (e.g. breastfeeding, art) is generally allowed.

C2: Harassment & Bullying:
Core Value: Foster a safe and respectful environment where users are protected from harassment, intimidation, and privacy violations.
[BLOCKED] No bullying, harassment or sexual harassment
[BLOCKED] No sharing others' private info or images of them in private spaces without consent
[BLOCKED] Remove content if the person depicted asks you to

C3: Threats, Violence & Harm:
Core Value: Prevent the promotion and glorification of violence, self-harm, and dangerous activities to ensure user safety.
[BLOCKED] Content involving bullying, harassment, or sexual harassment should be flagged.
[BLOCKED] Content sharing others' private info or images of them in private spaces without consent should be flagged.
[BLOCKED] Content should be removed if the person depicted asks you to.
[BLOCKED] Content abusing reporting systems to harass others should be flagged.

C4: False & Deceptive Information:
Core Value: Maintain a trustworthy platform by combating the spread of false information, deception, and fraudulent activities.
[BLOCKED] Content encouraging or depicting violence, dangerous behavior, or animal abuse should be flagged.
[BLOCKED] Content glorifying self-harm, suicide, eating disorders, or other self-injury should be flagged.
[BLOCKED] Imminent threats of violence should be reported to authorities.


C5: Illegal/Regulated Activities:
Core Value: Comply with legal requirements and prevent the promotion of illegal activities to protect users and society at large.
[BLOCKED] Content promoting illegal activity like selling drugs, weapons, or exploitation should be flagged.
[BLOCKED] Content containing unauthorized promotion of regulated goods like gambling, alcohol, or tobacco should be flagged.
[BLOCKED] Content violating the law where the user is located should be removed.

C6: Hateful Content & Extremism:
Core Value: Stand against hatred, discrimination, and extremism to create an inclusive community that respects diversity.
[BLOCKED] Content from terrorist groups, hate groups, or violent extremists should be flagged.
[BLOCKED] Content containing hate speech or demeaning or discriminating against protected groups should be flagged.
[BLOCKED] Content advocating terrorism or violent extremism should be flagged.
<END HARMFUL CATEGORIES EXPLANATIONS>

**Provide the moderation result in the following JSON format:**

MODERATION_RESULT = {{
"C1(Sexual Content)": boolean,
"C2(Harassment & Bullying)": boolean,
"C3(Threats, Violence & Harm)": boolean,
"C4(False & Deceptive Information)": boolean,
"C5(Illegal/Regulated Activities)": boolean,
"C6(Hateful Content & Extremism)": boolean
}}
**Set the value to true ONLY for the most relevant categories found in the video. If no harmful content is detected, set all values to false.**
**The first line must be the summarization the content of the video, beginning with "VIDEO_CONTENT:"**
**The second line must be the JSON format of "MODERATION_RESULT", beginning with "MODERATION_RESULT:"**
**<OPTIONAL>For each category flagged as true, provide a brief explanation of why it was flagged and list the specific policy violations within that category in the third line, beginning with "VIOLATE_REASON:"**'''

"""