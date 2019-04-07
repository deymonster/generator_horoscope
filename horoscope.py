import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []
    

    for i in range (total_num):
        forecast = ""
        
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)
            
            full_sentence = f"{t.capitalize()} {a} {p}."
            
            if j!= num_sentences -1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            

        prophecies.append(forecast)
        
        # lu_advices.append()
        # lu_promises.append()
    return prophecies, times, advices, promises





    # i = 0
    # while i < total_num:
    #     j = 0
    #     forecast = ""
    #     while j < num_sentences:
    #         t = random.choice(times)
    #         a = random.choice(advices)
    #         p = random.choice(promises)

    #         full_sentence = t.title() + " " + a + " " + p + "."
    #         if j != num_sentences - 1:
    #             full_sentence = full_sentence + " "

    #         forecast = forecast + full_sentence
    #         j = j + 1

    #     prophecies.append(forecast)
    #     i = i + 1

    # return prophecies
    # old version

