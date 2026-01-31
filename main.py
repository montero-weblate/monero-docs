def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def multiply(arg1, arg2):
        "Multiply 2 numbers"
        return arg1 * arg2

    @env.macro
    def i18n_macros_string(key_path):
        "Get translation for current page locale"
        locale = env.variables.get('i18n_page_locale', 'en')
        lang_dict = env.variables.get(locale, {})
        for key in key_path.split('.'):
            lang_dict = lang_dict.get(key, {})
        return lang_dict

    @env.macro
    def i18n_str(key_path):
        # we have "es"
        # https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/
        lang = env.conf['theme']['language']
        # conf is for mkdocs.yml , use variables
        result = env.variables[lang]

        # es.x.y is top level like config.x.y

        # some.keys.are.nested
        # the for loop will set translations 
        # result = result.notices returns the list
        # result = result.outdatedTranslation skips over notices and returns the value

        for key in key_path.split('.'):
            result = result[key]
        
        return result