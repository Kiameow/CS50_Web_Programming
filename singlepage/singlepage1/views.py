from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return render(request, "singlepage1/index.html")

texts = ["'Hamlet' is a tragic play written by William Shakespeare, believed to have been written between 1599 and 1601. The play is set in Denmark and tells the story of Prince Hamlet, who is deeply affected by the sudden death of his father, King Hamlet. Shortly after King Hamlet's death, his brother Claudius marries Queen Gertrude and becomes the new king.",

"Hamlet is visited by the ghost of his father, who reveals that he was murdered by Claudius. The ghost urges Hamlet to seek revenge. Hamlet, tormented by doubt and indecision, feigns madness to investigate the truth. He devises a plan to confirm Claudius's guilt by staging a play that mirrors the alleged murder. When Claudius reacts with guilt, Hamlet becomes convinced of his uncle's treachery.",

"However, Hamlet's internal struggles and complex relationships lead to a series of tragic events. Ophelia, Hamlet's love interest, goes mad and drowns. Laertes, Ophelia's brother, seeks revenge against Hamlet. A duel is arranged between Hamlet and Laertes, where both are fatally poisoned. Before his death, Hamlet kills Claudius and names Prince Fortinbras of Norway as his successor.",

"The play explores themes of revenge, betrayal, madness, and the complexity of human emotions. Hamlet's character is known for his philosophical soliloquies, including the famous To be, or not to be speech, which reflects his contemplation of life and death. Hamlet is widely regarded as one of Shakespeare's greatest works and continues to be studied and performed worldwide."]
def section(request, num):
  if 1 <= num <= 4:
    return HttpResponse(texts[num-1]);