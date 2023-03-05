function containsSubstring(string, substring){
  const sub_length = substring.length

  for (let i = 0; i < (string.length - sub_length + 1); i++) {
    var my_slice = string.slice(i, i + sub_length)
    if (my_slice == substring) {
      return true
    }
  }

  return false
}

console.log(containsSubstring("https://tabs.ultimate-guitar.com/tab/misc-soundtrack/a-mighty-wind-a-kiss-at-the-end-of-the-rainbow-chords-213444", "tabs.ultimate-guitar.com"))
console.log(containsSubstring("https://tabs.ultimate-guitar.com/tab/misc-soundtrack/a-mighty-wind-a-kiss-at-the-end-of-the-rainbow-chords-213444", "tabs.ultimate-guitar.coms12"))
