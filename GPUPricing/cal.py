import json

def calculate_average(fps1, fps2):
    if fps1 and fps2:
        return (float(fps1) + float(fps2)) / 2
    elif fps1:
        return float(fps1)
    elif fps2:
        return float(fps2)
    else:
        return 0

def main():
    # Read the JSON file
    with open('used_data.json', 'r') as json_file:
        data = json.load(json_file)
    
    # Calculate the average and out value for each object
    for item in data:
        avg_fps = item.get('fps2')#calculate_average(item.get('fps1'), item.get('fps2'))
        if avg_fps:
            avg_fps = float(avg_fps)
        else:
            avg_fps = 0
        price = item.get('price')
        if price:
            price = float(price)
        else:
            price = 1000000.0
        out = avg_fps / price * 1000
        # item['name'] = item.get('name')
        item['framePer1k'] = out
    
    # Sort the objects based on the out value
    sorted_data = sorted(data, key=lambda x: x['framePer1k'], reverse=True)
    
    # Print the sorted objects
    # for item in sorted_data:
    #     print(json.dumps(item, indent=4))
    for item in sorted_data:
        name = item.get('name', 'N/A')
        fps2 = item.get('fps2', 'N/A')
        price = item.get('price', 'N/A')
        out = item.get('framePer1k', 0)
        print(f"Name: {name}, FPS-1080p(Medium): {fps2}, Price: {price}, Frame-Per-1k: {out:.5f}")

if __name__ == "__main__":
    main()
