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