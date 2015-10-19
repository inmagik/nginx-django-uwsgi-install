from jinja2 import Environment, FileSystemLoader
import json
import sys
import os


def main(cfg_path, out_path):
    
    env = Environment(loader=FileSystemLoader('templates', followlinks=True))

    with open(cfg_path) as f:
        CFG = json.load(f)

    if not os.path.isdir(out_path):
        os.mkdir(out_path)

    for name in ['nginx.conf.template', 'uwsgi.ini.template', 'supervisor.conf.template']:
        template = env.get_template(name)
        rendered = template.render(CFG=CFG)
        dest_name = os.path.join(out_path, name.replace(".template", ""))
        with open(dest_name, "wb") as w:
            w.write(rendered)


if __name__ == '__main__':
    cfg_path = sys.argv[1]
    out_path = sys.argv[2]
    main(cfg_path, out_path)

