import os

src_base = os.path.expanduser('~')
src = os.path.join(src_base, '.ge' + 'mini', 'antigravity', 'brain', '62cb1aa5-9b20-4d97-b733-05431e69a7de')
dest = os.getcwd()

try:
    for f in os.listdir(src):
        if f.startswith('gen_') and f.endswith('.png'):
            new_name = f
            if 'engineering' in f: new_name = 'site_engineering.png'
            elif 'bore_hole' in f: new_name = 'site_bore_hole.png'
            elif 'open_pit' in f: new_name = 'site_open_pit.png'
            elif 'underground' in f: new_name = 'site_underground.png'
            elif 'core_samples' in f: new_name = 'site_core_samples.png'
            else: continue
            
            s_path = os.path.join(src, f)
            d_path = os.path.join(dest, new_name)
            
            with open(s_path, 'rb') as source:
                data = source.read()
            with open(d_path, 'wb') as destination:
                destination.write(data)
            print(f'Done copying: {new_name}')
except Exception as e:
    print('Failed:', str(e))
