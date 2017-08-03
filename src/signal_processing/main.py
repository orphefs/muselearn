def video_categories_list(service):  # See full sample for function
    results = service.videoCategories().list().execute()

    print(results)


video_categories_list(service,
                      part='snippet',
                      regionCode='US')
