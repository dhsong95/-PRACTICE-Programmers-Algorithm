def solution(genres, plays):
    # 음악의 고유번호가 저장된 앨범 리스트
    album = list()

    # 장르-재생 횟수에 대한 해시 테이블
    genre_count = {genre: 0 for genre in set(genres)}
    # 장르-(음악 고유 번호, 재생 회수) 리스트에 대한 해시 테이블
    genre_music = {genre: list() for genre in set(genres)}

    # 해시 테이블 구성
    for music, (genre, play) in enumerate(zip(genres, plays)):
        genre_count[genre] += play
        genre_music[genre].append((music, play))

    # 재생 회수를 기반으로 장르 순서 정렬
    genre_sorted = [g for g, _ in sorted(genre_count.items(), key=lambda x: -x[1])]
    for genre in genre_sorted:
        # 재생 회수를 기반으로 음악 고유 번호 순서 정렬
        music_sorted = [m for m, _ in sorted(genre_music[genre], key=lambda x: -x[1])]
        if len(music_sorted) == 1:
            album += music_sorted
        else:
            album += music_sorted[:2]

    return album


if __name__ == '__main__':
    assert solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) == [4, 1, 3, 0]
