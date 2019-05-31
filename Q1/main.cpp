#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>

int main()
{
    std::vector<int> v1(100);
    std::generate(v1.begin(), v1.end(), []{static int i{}; return ++i;});

    std::vector<int> v2(10);
    std::generate(v2.begin(), v2.end(), []{static int i{}; return ++i;});

    v1.insert(v1.end(), v2.begin(), v2.end());
    std::for_each(v1.begin(), v1.end(), [](int n){std::cout << n << " ";});
    std::cout << "\n\n\n*********************************************\n\n\n";

    std::vector<int> odd_vec(v1.size());
    auto vv = std::copy_if(v1.begin(), v1.end(), odd_vec.begin(), [](int i){return i%2;});
    odd_vec.resize(std::distance(odd_vec.begin(),vv));
    std::for_each(odd_vec.begin(), odd_vec.end(), [](int n){std::cout << n << " ";});
    std::cout << "\n\n\n*********************************************\n\n\n";

    std::vector<int> reverse_vec(v1.size());
    std::reverse_copy(v1.begin(), v1.end(), reverse_vec.begin());
    std::for_each(reverse_vec.begin(), reverse_vec.end(), [](int n){std::cout << n << " ";});
    std::cout << "\n\n\n*********************************************\n\n\n";

    std::sort(std::execution::par, v2.begin(), v2.end());
    std::sort(v2.begin(), v2.end());
    std::for_each(v2.begin(), v2.end(), [](int n){std::cout << n << " ";});

    return 0;
}
