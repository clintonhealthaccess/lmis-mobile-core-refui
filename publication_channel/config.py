repo_url = "http://52.78.205.75:8081/"
repo_name = "OpenLMIS Mobile Ref UI repo"
repo_icon = "fdroid-icon.png"
repo_description = """
This is a repository of apps to be used with F-Droid. Applications in this
repository are either official binaries built by the original application
developers, or are binaries built from source by the admin of f-droid.org
using the tools on https://gitlab.com/u/fdroid.
"""

# As above, but for the archive repo.
# archive_older sets the number of versions kept in the main repo, with all
# older ones going to the archive. Set it to 0, and there will be no archive
# repository, and no need to define the other archive_ values.
archive_older = 3
archive_url = "https://f-droid.org/archive"
archive_name = "My First F-Droid Archive Demo"
archive_icon = "fdroid-icon.png"
archive_description = """
The repository of older versions of applications from the main demo repository.
"""

sdk_path = "$ANDROID_HOME"

build_tools = "19.1.0"

keystore = "keystore.jks"

keystorepass = "this need to be replaced"

keypass = "this need to be replaced"

repo_keyalias = "this need to be replaced"

keydname = "CN=this need to be replaced, OU=F-Droid"