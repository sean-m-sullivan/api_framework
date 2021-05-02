# Redhat Communties of Practice API Framework Collection

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Code style: flake8](https://img.shields.io/badge/Code%20style-flake8-orange)
<!-- Further CI badges go here as above -->

This is a Framework Collection only. The purpose is to provide 80% of the code needed to interact with any given api. It is based off the Ansible Tower/Automation Hub Api, but most of the functions should be relatively close to what would be needed. This provides a framework for creating modules that will interact with an API.

This Ansible collection provides a framework for a collection to allow for easy interaction with an API via Ansible playbooks.

This code will not work in its current form. Many of the functions will need tweaked in order to work correctly. For example assocations may not be present in a particular API, or they may use other naming/id conventions.

The rest of this Readme also provides a framework for content that should be in a collection Readme, and is meant as an example only.

## Included content

Click the `Content` button to see the list of content included in this collection.

## Installing this collection

You can install the redhat_cop api_framework collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install redhat_cop.api_framework

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: redhat_cop.api_framework
    # If you need a specific version of the collection, you can specify like this:
    # version: ...
```

## Using this collection
Define following vars here, or in `configs/auth.yml`
`server: http://apiserver.com`

You can also specify authentication by setting the following variables:
 - `token`, `oauthtoken`

The OAuth2 token is the only method. You can obtain the token through through the web interface if applicable

These can be specified via (from highest to lowest precedence):

 - direct role variables as mentioned above

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Release and Upgrade Notes
For details on changes between versions, please see [the changelog for this collection](CHANGELOG.rst).

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [API Framework collection repository](https://github.com/redhat-cop/api_framework).
More information about contributing can be found in our [Contribution Guidelines.](https://github.com/redhat-cop/api_framework/blob/devel/.github/CONTRIBUTING.md)

## Licensing
GNU General Public License v3.0 or later.

See [LICENCE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

All content in this folder is licensed under the same license as Ansible,
which is the same as license that applied before when the base for this
code was derived form the [AWX.AWX](https://galaxy.ansible.com/awx/awx) collection.
