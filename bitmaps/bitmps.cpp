#include <iostream>
#include <fstream>

struct BitmapHeaders {
    int file_size {0};
    int data_offset {0};
    int info_header_size {0};
    int width {0};
    int height {0};
    short planes {0};
    short bits_per_pixel {0};
    int compression {0};
    int image_size {0};
    int x_pixels_per_m {0};
    int y_pixels_per_m {0};
    int colors_used {0};
    int colors_important {0};
};

struct Pixel {
    unsigned char b {};
    unsigned char g {};
    unsigned char r {};
};

static int read_int(const unsigned char* bytes) {
    return *reinterpret_cast<const int *>(bytes);
}

static short read_short(const unsigned char* bytes) {
    return *reinterpret_cast<const short *>(bytes);
}


static bool load_raw_file_data(const char* path, unsigned char* file_data, const int size, const int pos = 0) {
    std::ifstream file(path, std::ios::binary);
    if (!file) { return false; }
    file.seekg(pos);
    file.read(reinterpret_cast<char*>(file_data), size);
    return file.gcount() == size;
}

static bool check_signature(const unsigned char* sign) {
    return *sign == 'B' && *(sign+1) == 'M';
}

static void map_header(const unsigned char* source, BitmapHeaders& dest) {
    dest.file_size =         read_int(source + 2);
    dest.data_offset =       read_int(source + 10);
    dest.info_header_size =  read_int(source + 14);
    dest.width =             read_int(source + 18);
    dest.height =            read_int(source + 22);
    dest.planes =            read_short(source + 26);
    dest.bits_per_pixel =    read_short(source + 28);
    dest.compression =       read_int(source + 30);
    dest.image_size =        read_int(source + 34);
    dest.x_pixels_per_m =    read_int(source + 38);
    dest.y_pixels_per_m =    read_int(source + 42);
    dest.colors_used =       read_int(source + 46);
    dest.colors_important =  read_int(source + 50);
}

static void print_headers(const BitmapHeaders& h) {
    std::cout << "File size: " << h.file_size << std::endl;
    std::cout << "Data offset: " << h.data_offset << std::endl;
    std::cout << "Info header size: " << h.info_header_size << std::endl;
    std::cout << "Width: " << h.width << std::endl;
    std::cout << "Height: " << h.height << std::endl;
    std::cout << "Planes: " << h.planes << std::endl;
    std::cout << "Bits per pixel: " << h.bits_per_pixel << std::endl;
    std::cout << "Compression: " << h.compression << std::endl;
    std::cout << "Image size: " << h.image_size << std::endl;
    std::cout << "X pixels per m: " << h.x_pixels_per_m << std::endl;
    std::cout << "Y pixels per m: " << h.y_pixels_per_m << std::endl;
    std::cout << "Colors used: " << h.colors_used << std::endl;
    std::cout << "Colors important: " << h.colors_important << std::endl;
}

static Pixel get_pixel(const unsigned char* data, const int x, const int y, const int row_size) {
    const unsigned char* p = data + y * row_size + x * 3;
    Pixel pixel;
    pixel.b = p[0];
    pixel.g = p[1];
    pixel.r = p[2];
    return pixel;
}

static void print_pixel(const char* name, const Pixel& pixel) {
    std::cout << name << " R: " << static_cast<int>(pixel.r)
                      << " G: " << static_cast<int>(pixel.g)
                      << " B: " << static_cast<int>(pixel.b) << std::endl;
}

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "lena.bmp";

    unsigned char headers_raw[54];
        if (!load_raw_file_data(path, headers_raw, 54)) {
        std::cerr << "couldnt open a file" << std::endl;
        return 1;
    }
    if (!check_signature(headers_raw)) {
        std::cerr << "not a .bmp file" << std::endl;
        return 1;
    }
    std::cout << "loaded 54 bytes" << std::endl;

    BitmapHeaders headers;
    map_header(headers_raw, headers);
    print_headers(headers);
    if (headers.bits_per_pixel != 24 || headers.height <= 0) {
        std::cerr << "Only 24-bit bottom-up BMP is supported" << std::endl;
        return 1;
    }

    const int width = headers.width;
    const int height = headers.height;
    const int row_size = (width * 3 + 3) / 4 * 4;
    const int data_size = row_size * height;

    unsigned char* data = new unsigned char[data_size];
    if (!load_raw_file_data(path, data, data_size, headers.data_offset)) {
        std::cerr << "Cannot read pixel data" << std::endl;
        delete[] data;
        return 1;
    }

    print_pixel("Bottom-left: ",  get_pixel(data, 0,         0,          row_size));
    print_pixel("Bottom-right:",  get_pixel(data, width - 1, 0,          row_size));
    print_pixel("Top-left:    ",  get_pixel(data, 0,         height - 1, row_size));
    print_pixel("Top-right:   ",  get_pixel(data, width - 1, height - 1, row_size));

    delete[] data; //удалить заполненное место в памяти new
    return 0;
}