import random

NAMES_MALE = ["كريم", "أحمد", "حيدر", "مصطفى", "علي", "يوسف", "عمر", "سامي", "باسم", "طارق"]
NAMES_FEMALE = ["سارة", "زينب", "منى", "ليلى", "نور", "هدى", "رؤى", "ياسمين", "أمل", "دعاء"]
PLACES = ["القاهرة", "بغداد", "الإسكندرية", "البصرة", "دمشق", "عمّان", "الموصل", "أسوان", "النجف", "بيروت"]
RELATIONS = ["أبوها", "أخوها الكبير", "جدتها", "جارهم القديم", "صديق طفولتها", "خالها", "معلمها بالمدرسة"]
OBJECTS = ["دفتر قديم", "صورة بالأبيض والأسود", "خاتم فضة", "رسالة ممزقة", "مفتاح صدئ", "ساعة يد متوقفة"]
EMOTIONS = ["حزن دفين", "أمل مفاجئ", "ندم قديم", "فرحة غامرة", "خوف من المجهول", "شوق لأيام راحت"]

def pick_person():
    if random.random() < 0.5:
        return random.choice(NAMES_MALE), "هو"
    return random.choice(NAMES_FEMALE), "هي"

SOCIAL_TEMPLATES = [
    "في حي قديم وسط {place}، كان في بيت بسيط يعيش فيه {name} مع عيلته.",
    "{name} كان/كانت بيشتغل/بتشتغل بجد كل يوم، عشان يوفر/توفر مستقبل أحسن لأولاده/لأولادها.",
    "لكن الظروف كانت صعبة، والمصاريف بتزيد كل شهر عن اللي قبله.",
    "{relation} كان دايمًا بيقف جنبه/جنبها وقت الضيق، حتى لو الكلام مكانش سهل.",
    "يوم من الأيام، لقى/لقت {name} {object} كان مخبّي من زمان في دولاب قديم.",
    "الـ{object} فتح/فتحت باب ذكريات قديمة، وحسّ/حست بـ{emotion} مفاجئ.",
    "قرر/قررت إنه/إنها يواجه/تواجه اللي فات، ويحكي/تحكي الحقيقة لعيلته كلها.",
    "الكلام مكانش سهل، لكن الصدق كان أهم من أي حاجة تانية.",
    "بعد فترة، الحياة رجعت لطبيعتها، لكن العلاقة بين الكل بقت أقوى من الأول.",
]

SUSPENSE_TEMPLATES = [
    "في ليلة باردة في {place}، سمع/سمعت {name} صوت غريب جاي من الطابق التحت.",
    "القلب كان بيدق بسرعة، والبيت كله كان ساكت غير صوت الساعة الحايطة.",
    "قرر/قررت ينزل/تنزل يشوف/تشوف مصدر الصوت، رغم الخوف اللي حاسس/حاسة بيه.",
    "لقى/لقت الباب الخلفي مفتوح، والريح بتحرك الستارة ببطء.",
    "على الأرض كانت واقفة/واقف {object}، حاجة معرفش/معرفتش حد حطها هناك.",
    "فجأة، صوت خطوات بدأ يقرب من ناحيته/ناحيتها في الضلمة.",
    "طلع/طلعت إنه/إنها {relation}، جاي/جاية يشوف/تشوف عليه بعد غيبة طويلة.",
    "الخوف اتحول لضحكة ارتياح، وقعدوا يتكلموا لحد الصبح.",
]

HISTORICAL_TEMPLATES = [
    "زمان في {place}، قبل سنين طويلة، كانت الحياة مختلفة تمامًا عن دلوقتي.",
    "{name} كان/كانت من الناس اللي عاصرت أحداث كبيرة غيّرت شكل المدينة.",
    "كانت الأيام صعبة، لكن الناس كانت متكاتفة أكتر بكتير.",
    "{relation} كان بيحكي كل ليلة قصص عن أيام زمان، والصغيرين حواليه بيسمعوا بانبهار.",
    "من ضمن الحاجات اللي فضلت من الزمن ده، {object} كان شاهد على كل حاجة حصلت.",
    "لما {name} كبر/كبرت، فهم/فهمت قيمة اللي اتعلمه من الماضي.",
    "القصة دي فضلت متناقلة في العيلة جيل ورا جيل، عشان محدش ينسى.",
]

GENRE_POOLS = {
    "social": SOCIAL_TEMPLATES,
    "suspense": SUSPENSE_TEMPLATES,
    "historical": HISTORICAL_TEMPLATES,
}

TITLES = [
    "حكاية من الحي القديم", "سر البيت الكبير", "ذكريات ما بتتنسيش",
    "ليلة في {place}", "وريث الحكاية", "بين الماضي والحاضر",
]

def fill(template, name, pronoun_word, place, relation, obj, emotion):
    return (
        template
        .replace("{name}", name)
        .replace("{place}", place)
        .replace("{relation}", relation)
        .replace("{object}", obj)
        .replace("{emotion}", emotion)
    )

def generate(min_scenes=130):
    name, _ = pick_person()
    place = random.choice(PLACES)
    relation = random.choice(RELATIONS)
    obj = random.choice(OBJECTS)
    emotion = random.choice(EMOTIONS)

    title = random.choice(TITLES).replace("{place}", place)

    scenes = []
    genres = list(GENRE_POOLS.keys())
    random.shuffle(genres)

    # نبني القصة من مزيج الأنواع التلاتة، ونكرر التمبلتس بتنويع
    # المكوّنات (أسماء/أماكن/أغراض مختلفة) لحد ما نوصل للعدد المطلوب
    while len(scenes) < min_scenes:
        genre = random.choice(genres)
        templates = GENRE_POOLS[genre]
        # كل دورة نجدد الأسماء والأماكن عشان التنويع
        name, _ = pick_person()
        place = random.choice(PLACES)
        relation = random.choice(RELATIONS)
        obj = random.choice(OBJECTS)
        emotion = random.choice(EMOTIONS)
        for t in templates:
            scenes.append(fill(t, name, _, place, relation, obj, emotion))
            if len(scenes) >= min_scenes:
                break

    return {"title": title, "scenes": scenes}

if __name__ == "__main__":
    story = generate()
    print(story["title"], "-", len(story["scenes"]), "مشهد")

import json, os as _os

HISTORY_FILE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "story_history.json")

def _load_history():
    if _os.path.exists(HISTORY_FILE):
        try:
            return json.load(open(HISTORY_FILE))
        except Exception:
            return []
    return []

def _save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history[-30:], f, ensure_ascii=False)  # آخر 30 قصة بس

def generate_unique(min_scenes=130, max_tries=15):
    history = _load_history()
    for _ in range(max_tries):
        story = generate(min_scenes=min_scenes)
        signature = story["title"] + story["scenes"][0]
        if signature not in history:
            history.append(signature)
            _save_history(history)
            return story
    # لو كل المحاولات كررت، رجّع آخر واحدة على أي حال
    return story
