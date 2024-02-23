import re
import config

password_pattern = re.compile(config.PASSWORD_REGEX)


def scan_contents(repo):
    contents = repo.get_contents("/")
    for content in contents:
        if content.type == "dir":
            scan_contents(repo.get_contents(content.path))

        elif content.type == "file":
            try:
                file_content = content.decoded_content.decode('utf-8')
                if re.findall(password_pattern, file_content):
                    print(f"secret password found in the file \"{content.path}\"\n")
            except Exception as e:
                print(f"Error processing {content.path}: {e}")
