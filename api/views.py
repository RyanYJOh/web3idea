from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Verbs
import json

def home(request):
    return render(request, 'home.html')

def getVerb(request):
    verb = Verbs.objects.all().order_by('?')[0].verb
    print('this verb :', verb)
    context = json.dumps({
        'verb' : verb,
    }) 
    print(type(context))
    return JsonResponse(context, safe=False)

def addVerbs(request):
    verbs = ["Accept"	,
"Add"	,
"Admire"	,
"Admit"	,
"Give Advice"	,
"Agree"	,
"Alert"	,
"Allow"	,
"Amuse"	,
"Analyze"	,
"Applaud"	,
"Appreciate"	,
"Get Appreciated"	,
"Argue"	,
"Get Arrested"	,
"Ask"	,
"Attack"	,
"Attract"	,
"Bake"	,
"Bang"	,
"Bathe"	,
"Battle"	,
"Beg"	,
"Behave"	,
"Belong"	,
"Bless"	,
"Blink"	,
"Blush"	,
"Boast"	,
"Get Bored"	,
"Borrow"	,
"Lend"	,
"Bow"	,
"Box"	,
"Brake"	,
"Breathe"	,
"Get Bruised"	,
"Brush"	,
"Burn"	,
"Buzz"	,
"Calculate"	,
"Call"	,
"Carry"	,
"Challenge"	,
"Change"	,
"Charge"	,
"Chase"	,
"Cheat"	,
"Check"	,
"Cheer"	,
"Chew"	,
"Clap"	,
"Clean"	,
"Collect"	,
"Comb"	,
"Communicate"	,
"Compete"	,
"Earn"	,
"Complain"	,
"Confess"	,
"Consider"	,
"Continue"	,
"Copy"	,
"Cough"	,
"Count"	,
"Crash"	,
"Crawl"	,
"Cry"	,
"Dance"	,
"Decide"	,
"Decorate"	,
"Delay"	,
"Delight"	,
"Deliver"	,
"Describe"	,
"Deserve"	,
"Destroy"	,
"Develop"	,
"Disappear"	,
"Disapprove"	,
"Get Approved"	,
"Divide"	,
"Conquer"	,
"Dream"	,
"Get Dressed"	,
"Drop"	,
"Educate"	,
"Embarrass"	,
"Get Embarrassed"	,
"Empty"	,
"Encourage"	,
"End"	,
"Enjoy"	,
"Entertain"	,
"Escape"	,
"Get Entertained"	,
"Take Exam"	,
"Get Excited"	,
"Excuse"	,
"Exercise"	,
"Work Out"	,
"Exist"	,
"Expand"	,
"Explain"	,
"Face"	,
"Fail"	,
"Fasten Your Seatbelt"	,
"Fear"	,
"Fill"	,
"Fire"	,
"Get Fired"	,
"Fix"	,
"Flow"	,
"Fold"	,
"Get Fooled"	,
"Fool"	,
"Follow"	,
"Found"	,
"Fry"	,
"Gather"	,
"Gaze"	,
"Glow"	,
"Grab"	,
"Grease"	,
"Greet"	,
"Groan"	,
"Guarantee"	,
"Guard"	,
"Guess"	,
"Guide"	,
"Hand"	,
"Hang"	,
"Hang Out"	,
"Hang Up"	,
"Heal"	,
"Help"	,
"Get Help"	,
"Hook"	,
"Hop"	,
"Hope"	,
"Hug"	,
"Hum"	,
"Hurry"	,
"Work Hard"	,
"Identify"	,
"Ignore"	,
"Imagine"	,
"Improve"	,
"Increase"	,
"Influence"	,
"Inform"	,
"Instruct"	,
"Get Interested"	,
"Interfere"	,
"Interrupt"	,
"Introduce"	,
"Invent"	,
"Invite"	,
"Jog"	,
"Join"	,
"Make Jokes"	,
"Judge"	,
"Juggle"	,
"Jump"	,
"Kick"	,
"Kiss"	,
"Knit"	,
"Knock"	,
"Knot"	,
"Laugh"	,
"Launch"	,
"Lick"	,
"Lighten"	,
"Like"	,
"Listen"	,
"Live"	,
"Load"	,
"Lock"	,
"Look"	,
"Love"	,
"Love"	,
"Love"	,
"Love"	,
"Love"	,
"Love"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Manage"	,
"Mark"	,
"Marry"	,
"Measure"	,
"Meddle"	,
"Memorize"	,
"Mend"	,
"Don'T Mess Up"	,
"Miss"	,
"Mix"	,
"Moan"	,
"Mourn"	,
"Move"	,
"Take Notes"	,
"Count"	,
"Object"	,
"Observe"	,
"Obtain"	,
"Open"	,
"Order"	,
"Own"	,
"Pack"	,
"Paint"	,
"Park"	,
"Fart"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pass"	,
"Paste"	,
"Peel"	,
"Peep"	,
"Perform"	,
"Pick"	,
"Pinch"	,
"Plan"	,
"Don'T Play"	,
"Plug"	,
"Point"	,
"Polish"	,
"Possess"	,
"Post"	,
"Pour"	,
"Practice"	,
"Pray"	,
"Pray"	,
"Pray"	,
"Pray"	,
"Prepare"	,
"Press"	,
"Pretend"	,
"Print"	,
"Produce"	,
"Make Promises"	,
"Protect"	,
"Use Protection"	,
"Provide"	,
"Pull"	,
"Push"	,
"Question"	,
"Queue"	,
"Race"	,
"Raise"	,
"Reach"	,
"Realize"	,
"Recognize"	,
"Receive"	,
"Record"	,
"Reduce"	,
"Reflect"	,
"Regret"	,
"Reject"	,
"Rejoice"	,
"Relax"	,
"Release"	,
"Rely"	,
"Remember"	,
"Remind"	,
"Repair"	,
"Repeat"	,
"Replace"	,
"Report"	,
"Reitre"	,
"Request"	,
"Rescue"	,
"Return"	,
"Rhyme"	,
"Risk"	,
"Roll"	,
"Rub"	,
"Rush"	,
"Sail"	,
"Satisfy"	,
"Save"	,
"Scrape"	,
"Scratch"	,
"Scream"	,
"Screw"	,
"Scrub"	,
"Search"	,
"Separate"	,
"Serve"	,
"Settle"	,
"Share"	,
"Shave"	,
"Shiver"	,
"Shock"	,
"Shop"	,
"Shrug"	,
"Sigh"	,
"Sign"	,
"Skip"	,
"Slap"	,
"Smell"	,
"Smile"	,
"Smile"	,
"Smile"	,
"Smile"	,
"Smile"	,
"Sneeze"	,
"Sniff"	,
"Snore"	,
"Snow"	,
"Soak"	,
"Soothe"	,
"Spark"	,
"Sparkle"	,
"Spell"	,
"Spill"	,
"Spot"	,
"Spray"	,
"Squeeze"	,
"Stare"	,
"Start"	,
"Steer"	,
"Stir"	,
"Stitch"	,
"Stop"	,
"Strengthen"	,
"Stretch"	,
"Strip"	,
"Subtract"	,
"Succeed"	,
"Succeed"	,
"Succeed"	,
"Supply"	,
"Surprise"	,
"Surround"	,
"Suspend"	,
"Switch"	,
"Talk"	,
"Tap"	,
"Taste"	,
"Tease"	,
"Tempt"	,
"Test"	,
"Thank"	,
"Thank"	,
"Thank"	,
"Tickle"	,
"Tie"	,
"Touch"	,
"Trade"	,
"Train"	,
"Travel"	,
"Tremble"	,
"Trust"	,
"Try"	,
"Try"	,
"Try"	,
"Try"	,
"Try"	,
"Try"	,
"Twist"	,
"Unite"	,
"Unlock"	,
"Unpack"	,
"Use Protection"	,
"Visit"	,
"Vanish"	,
"Wait"	,
"Walk"	,
"Wander"	,
"Wash"	,
"Watch"	,
"Wave"	,
"Whisper"	,
"Wink"	,
"Wish"	,
"Wonder"	,
"Rap"	,
"Rap"	,
"Yawn"	,
"Yell"	,
"Zip"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Poop"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Pee"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Work Hard"	,
"Be Happy"	,
"Be Naive"	,
"Be Creative"	,
"Build"	,
"Begin"	,
"Bet"	,
"Bid"	,
"Bite"	,
"Broadcast"	,
"Buy"	,
"Catch"	,
"Choose"	,
"Come"	,
"Cut"	,
"Dig"	,
"Draw"	,
"Dream"	,
"Dream"	,
"Dream"	,
"Drive"	,
"Drink"	,
"Eat"	,
"Eat"	,
"Feel"	,
"Find"	,
"Forget"	,
"Forget"	,
"Forget"	,
"Forget"	,
"Forgive"	,
"Freeze"	,
"Give"	,
"Go"	,
"Grow"	,
"Hear"	,
"Hide"	,
"Hold"	,
"Lead"	,
"Pay"	,
"Pay"	,
"Pay"	,
"Pay"	,
"Pay"	,
"Ride"	,
"Rise"	,
"Run"	,
"Say"	,
"Sell"	,
"Sing"	,
"Stink"	,
"Swim"	,
"Teach"	,
"Tear"	,
"Throw"	,
"Think"	,
"Think"	,
"Think"	,
"Think"	,
"Think"	,
"Understand"	,
"Wear"	,
"Wink"	,
"Write"	,
"Take Risk"	,
"Take Risk"	,
"Thank"	,
"Thank"	,
"Be Sure"	,
"Take Risk"	,
"Take Risk"	,
"Take Risk"	]
    verbs_v2 = ['Shitpost','Shitpost','Shitpost','Shitpost','Shitpost','Shitpost','Shitpost','Shitpost']
    for i in range(0, len(verbs_v2)):
        this_verb = verbs_v2[i]
        Verbs.objects.create(
            verb = this_verb
        )
        print(this_verb)
    
    return 