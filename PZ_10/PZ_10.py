def analyze_travel_agencies():
    """
    Анализирует предложения туристических агентств с использованием множеств.
    Определяет:
     1. Агентства с турами в Японию.
     2. Агентства без туров в ЮАР.
     3. Полный перечень туров.
    """
    voyazh = {"Мексика", "Канада", "Израиль", "Италия", "США"}
    reynatur = {"Англия", "Япония", "Канада", "ЮАР"}
    raduga = {"США", "Испания", "Швеция", "Австралия"}
    
    agencies_with_japan = []
    if "Япония" in voyazh:
        agencies_with_japan.append("Вояж")
    if "Япония" in reynatur:
        agencies_with_japan.append("РейнаТур")
    if "Япония" in raduga:
        agencies_with_japan.append("Радуга")
    
    print("1. Туры в Японию предлагают:")
    if agencies_with_japan:
        for agency in agencies_with_japan:
            print(f"   - {agency}")
    else:
        print("   Ни одно агентство не предлагает туры в Японию.")
    
    agencies_without_south_africa = []
    if "ЮАР" not in voyazh:
        agencies_without_south_africa.append("Вояж")
    if "ЮАР" not in reynatur:
        agencies_without_south_africa.append("РейнаТур")
    if "ЮАР" not in raduga:
        agencies_without_south_africa.append("Радуга")
    
    print("\n2. Туры в ЮАР НЕ предлагают:")
    if agencies_without_south_africa:
        for agency in agencies_without_south_africa:
            print(f"   - {agency}")
    else:
        print("   Все агентства предлагают туры в ЮАР.")
    
    all_tours = voyazh | reynatur | raduga  
    print("\n3. Полный список всех туров:")
    print("   " + ", ".join(sorted(all_tours)))

if __name__ == "__main__":
    analyze_travel_agencies()