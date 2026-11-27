# YouTube upload rules: metadata, disclosure, settings

Checked Nov 27, 2026. Sources are YouTube's own pages unless marked "third-party".

## 0. Feature access (check before upload)
- **Chapters and clickable description links need *advanced features*.** Custom thumbnails need phone verification (https://support.google.com/youtube/answer/9890437).
- New channels usually lack the channel history that unlocks advanced features. ID/video verification is the fast route ("usually takes 24 hours"), but not everyone is offered it (https://support.google.com/youtube/answer/9891124).

## 1. Description
- **Limit:** 5,000 characters (https://support.google.com/youtube/answer/57404). The API rejects `<` and `>` (https://developers.google.com/youtube/v3/docs/videos), so write "under $1", not "<$1".
- **Shown before "…more":** YouTube gives no number, only "before clicking 'Show more' on desktop or 'more' on mobile" (https://support.google.com/youtube/answer/12948449).
  - Desktop: about 100–160 characters (vidIQ, third-party). Search results may show only the first line (https://www.vidiq.com/blog/post/youtube-video-descriptions).
  - Mobile: the description opens as a separate sheet (https://9to5google.com/2020/11/04/youtube-descriptions-fullscreen/).
  - TV: it sits behind a Description button (https://support.google.com/youtube/answer/7583931). Chapters do show there (May 2026, https://www.socialmediatoday.com/news/youtube-adds-chapters-and-title-cards-to-ctv/820441/).
  - So the hook and main keyword go in the first ~120 characters.
- **Search:** "Search terms are matched with the video and the text in the description" (12948449). Ranking uses relevance (title, tags, description), engagement and quality (https://support.google.com/youtube/answer/16090438).
- **Suggested videos:** signals are viewing behaviour, likes, surveys and channel quality, not metadata (https://www.youtube.com/howyoutubeworks/product-features/recommendations/). Backlinko: keyword-optimised descriptions had no ranking impact (2017, https://backlinko.com/youtube-ranking-factors).
- **Structure:** hook with 1–2 keywords → short summary → chapters → sources → footer (not financial advice, AI voice, footage credits) → 2–3 hashtags. Each description should be unique (12948449).
- **Length:** vidIQ says "generally keep it under 1,000 characters". A source list may go past that.
- **Links:** no evidence that normal links reduce reach. Only links to rule-breaking content are banned (https://support.google.com/youtube/answer/9054257). Citing sources helps credibility.

## 2. Chapters (https://support.google.com/youtube/answer/9884579)
- "the first timestamp you list starts with 00:00".
- "at least three timestamps listed in ascending order".
- "The minimum length for video chapters is 10 seconds".
- Our chapters replace the automatic ones. Chapters are blocked while the channel "has any active strikes".
- **Google key moments** use the timestamps in the YouTube description and give them priority (https://developers.google.com/search/docs/appearance/structured-data/video).
- **Naming:** short and descriptive, no "Part 2". Hover titles cut off at about 49 characters (third-party: https://www.storyblocks.com/resources/tutorials/how-to-add-chapters-to-youtube-video). Aim for 5–8 chapters.

## 3. Tags
- YouTube: tags "play a minimal role in your video's discovery" but "can be useful if the content of your video is commonly misspelled" (https://support.google.com/youtube/answer/146402).
- **Limit:** 500 characters in total. Commas count, and so do the quotes added around tags with spaces (API docs above).
- **How many:**
  - vidIQ's test: tags alone didn't make a video findable (https://vidiq.com/blog/post/youtube-keyword-tags-2019-case-study/).
  - Ahrefs: the sweet spot is 200–300 characters (https://ahrefs.com/blog/youtube-tags).
  - Use 8–12 tags: the topic, common misspellings ("laundrymat") and the channel name.

## 4. Hashtags (https://support.google.com/youtube/answer/6390658)
- Hashtags can go in the title or description. "Up to three hashtags that are considered most engaging will appear by your video title."
- **The "15" rule is outdated.** The current text: "If a video or playlist has more than 60 hashtags, we'll ignore each hashtag on that content." Hashtags must be "directly related".
- Put 2–3 at the end of the description. Keep them out of the title, where they link viewers away.

## 5. Disclosure and monetisation
- **Altered/synthetic label** (https://support.google.com/youtube/answer/14328491): disclose "AI-generated or altered content that seems realistic". That covers content that:
  - "Makes a real person appear to say or do something they didn't do"
  - "Alters footage of a real event or place"
  - "Generates a realistic scene that didn't actually occur"
  - "Creates music that's the main focus of the video"
- **Exempt:** scripts, captions, and "Cloning one's own voice to create voice overs or dubs".
- The 2024 blog's "synthetically generating a person's voice to narrate a video" falls under likeness of a realistic person (https://blog.youtube/news-and-events/disclosing-ai-generated-content/).
- **A generic AI narrator is not presented as any real person, so answer "No"** (there's no realistic AI footage).
- YouTube may still auto-label "non-music AI-generated audio" in the expanded description. If it does, accept it: "Disclosing AI content alone won't limit a video's audience or impact its eligibility to earn money."
- **Inauthentic content** (renamed from "repetitious", Jul 15, 2025; https://support.google.com/youtube/answer/1311392):
  - Not monetised: "AI-generated content made with generic or unoriginal templates giving the impression of mass production".
  - Allowed: "Same intro and outro… but the bulk of your content is different". AI channels "remain eligible" (https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/).
- **AI personas, July 16, 2026** (https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/):
  - Not monetised: content that "presents itself as a human expert providing advice" on finances, e.g. "AI-generated podcast hosts offering financial guidance, investment tips" (1311392).
  - So the narrator never claims to be a person ("when I bought my route…"), never gives personal investment advice, and the description says the voice is AI.
- **Finance (YMYL):**
  - For "news, personal finance…" YouTube says it surfaces high-quality sources (recommendations page). Search quality means "expertise, authoritativeness, and trustworthiness" (16090438).
  - Information panels are automatic and "not used in any decisions about monetization" (https://support.google.com/youtube/answer/9004474).
  - A "not financial advice" line isn't required but supports the persona rule.
  - Avoid "get rich quick" framing (https://support.google.com/youtube/answer/2801973).

## 6. Other fields
- **Language:** helps "viewers find videos in their language" (https://support.google.com/youtube/answer/6304325). Auto captions use "the video's default language only" (https://support.google.com/youtube/answer/2734796). Set English for both.
- **Caption certification:** "never aired on television in the U.S."
- **Captions:** upload our exact `.srt` ("Upload file → With timing", 2734796). YouTube makes no search claim for captions.
- **Recording date/location:** optional (57404). Leave blank.
- **Category:** helps "viewers find your video more easily" (57404). There's no Finance category: choose **Education**, not the default People & Blogs or News & Politics.
- **Made for kids:** **No**. COPPA compliance is "your legal responsibility" (https://support.google.com/youtube/answer/9528076).
- **License:** **Standard YouTube License**. CC BY needs content that is "licenseable under the CC BY license", and stock footage isn't (https://support.google.com/youtube/answer/2797468).
- **Also:** allow embedding, and untick "Allow automatic Featured places" and automatic chapters (57404).
