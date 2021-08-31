google ={
    'culture':100,
    'challenges':100,
    'rating':5
}

amazon = {
    'culture':90,
    'perks':100,
    'rating':4

}

common_param_in_google_and_amazon = google.keys() & amazon.keys()

print(common_param_in_google_and_amazon)