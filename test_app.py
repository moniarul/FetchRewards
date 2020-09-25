from flask import Flask, abort, request, jsonify


app = Flask(__name__)


def is_pyramid(word):
    char_map = {}
    for ch in word:
        if ch in char_map:
            char_map[ch] += 1
        else:
            char_map[ch] = 1

    sorted_items = sorted(char_map.items(), key=lambda x: x[1])

    for i, item in enumerate(sorted_items):
        if item[1] != i + 1:
            return False

    return True


@app.route("/is_pyramid_word")
def is_pyramid_word():
    word = request.args.get("word")
    if word:
        return jsonify({"is_pyramid_word": is_pyramid(word)})
    else:
        abort(400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
